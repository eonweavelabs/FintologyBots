import datetime
from bson.objectid import ObjectId
from PIL import Image
import io
from Utils.database_conn import *


def upload_screenshot(filepath, application_id, product_id, flag=0):
    application_id=ObjectId(application_id)
    application = applications.find_one({"_id": ObjectId(application_id)})
    if not application:
        print("Application not found!")
        return
    
    for product in application.get("products", []):
        if product.get("credit_card") == product_id:
            if flag == 0:
                im = Image.open(filepath)
                image_bytes = io.BytesIO()
                im.save(image_bytes, format='PNG')
                screenshot_data = image_bytes.getvalue()
                update_data = {
                    "status": "processed",
                    "screenshot": screenshot_data
                }
            else:
                update_data = {
                    "status": "processed",
                    "screenshot": ""
                }
            applications.update_one(
                {
                    "_id": ObjectId(application_id),
                    "products.credit_card": product_id
                },
                {
                    "$set": {
                        "products.$.status": update_data["status"],
                        "products.$.screenshot": update_data["screenshot"]
                    }
                }
            )



