from dataclasses import dataclass, asdict
from datetime import date
from typing import List

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sp_api.api import Orders
from sp_api.base import SellingApiException, Marketplaces

import const


class GoogleSheets:
    def __init__(self, credentials_file: str, sheet_key: str, worksheet_name: str):
        self.credentials_file = credentials_file
        self.sheet_key = sheet_key
        self.worksheet_name = worksheet_name
        self.scope = [
            "https://spreadsheets.google.com/feeds",
        ]
        self.sheet_object = self._get_sheet_object()

    def _get_sheet_object(self) -> gspread.models.Worksheet:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials_file, self.scope
        )
        client = gspread.authorize(credentials)
        return client.open_by_key(self.sheet_key).worksheet(self.worksheet_name)

    def write_header_if_doesnt_exist(self, columns: List[str]) -> None:
        data = self.sheet_object.get_all_values()
        if not data:
            self.sheet_object.insert_row(columns)

    def append_rows(self, rows: List[List]) -> None:
        last_row_number = len(self.sheet_object.col_values(1)) + 1
        self.sheet_object.insert_rows(rows, last_row_number)


@dataclass
class AmazonOrder:
    order_id: str
    purchase_date: str
    order_status: str
    order_total: str
    payment_method: str
    marketplace_id: str
    shipment_service_level_category: str
    order_type: str


HEADER = [
    "AmazonOrderId",
    "PurchaseDate",
    "OrderStatus",
    "OrderTotal",
    "PaymentMethod",
    "MarketplaceId",
    "ShipmentServiceLevelCategory",
    "OrderType",
]


class AmazonScript:
    def __init__(self):
        google_sheets = GoogleSheets(
            "keys.json", const.GOOGLE_SHEETS_ID, const.GOOGLE_WORKSHEET_NAME
        )
        google_sheets.write_header_if_doesnt_exist(HEADER)
        self.get_orders_data_and_append_to_gs(google_sheets)

    def get_orders_data_and_append_to_gs(self, google_sheets: GoogleSheets) -> None:
        try:
            asin_data = self.get_order_from_sp_api()
            ready_rows = [list(asdict(row).values()) for row in asin_data]
            google_sheets.append_rows(ready_rows)
        except SellingApiException as e:
            print(f"Error: {e}")

    def get_order_from_sp_api(self) -> List[AmazonOrder]:
        client_config = dict(
            refresh_token=const.REFRESH_TOKEN,
            lwa_app_id=const.LWA_APP_ID,
            lwa_client_secret=const.CLIENT_SECRET,
            aws_secret_key=const.AWS_SECRET_KEY,
            aws_access_key=const.AWS_ACCESS_KEY,
            role_arn=const.ROLE_ARN,
        )
        res = Orders(credentials=client_config, marketplace=Marketplaces.IT)
        return self.convert_response_to_amazon_order_list(
            res.get_orders(CreatedAfter='2017-03-30', CreatedBefore=date.today().isoformat()).payload
        )

    @staticmethod
    def convert_response_to_amazon_order_list(
            response_payload: dict
    ) -> List[AmazonOrder]:
        amazon_order_list = []
        for item in response_payload.get("Orders"):
            amazon_order_list.append(
                AmazonOrder(
                    order_id=item.get("AmazonOrderId", ''),
                    purchase_date=item.get("PurchaseDate", ''),
                    order_status=item.get("OrderStatus", ''),
                    order_total=item.get("OrderTotal", {}).get("Amount", ""),
                    payment_method=item.get("PaymentMethod", ''),
                    marketplace_id=item.get("MarketplaceId", ''),
                    shipment_service_level_category=item.get("ShipmentServiceLevelCategory", ''),
                    order_type=item.get("OrderType", ''),
                )
            )
        return amazon_order_list


if __name__ == '__main__':
    print("Start script.")
    am = AmazonScript()
    print("Done.")
