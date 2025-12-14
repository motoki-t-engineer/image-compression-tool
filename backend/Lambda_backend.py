import json
import boto3
from PIL import Image
import io
import base64

# ===== 設定 =====
OUTPUT_BUCKET = "your-output-bucket-name"  # ここを変更
SIGNED_URL_EXPIRE = 3600  # 署名付きURLの有効期限（秒）
# =================

s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        # 1. POSTされた body を取得
        if event.get("isBase64Encoded"):
            body = base64.b64decode(event["body"])
        else:
            body = event["body"].encode()

        # 2. フロント側から送った JSON を想定（multipart を避ける簡単版）
        data = json.loads(body)
        filename = data["filename"]
        file_content = base64.b64decode(data["fileContent"])  # 画像は Base64 で送る
        format_ = data.get("format", "jpeg").lower()
        quality = int(data.get("quality", 80))

        # 3. 画像を PIL で読み込み
        img = Image.open(io.BytesIO(file_content))

        # JPEG の場合は RGB に変換
        if format_ == "jpeg":
            img = img.convert("RGB")

        # 4. メモリ上で圧縮・変換
        output_buffer = io.BytesIO()
        img.save(output_buffer, format=format_.upper(), quality=quality)
        output_buffer.seek(0)

        # 5. S3 にアップロード
        key = f"compressed/{context.aws_request_id}_{filename}"
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=key,
            Body=output_buffer.getvalue(),
            ContentType=f"image/{format_}"
        )

        # 6. 署名付きURLを生成
        signed_url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": OUTPUT_BUCKET, "Key": key},
            ExpiresIn=SIGNED_URL_EXPIRE
        )

        # 7. フロントに返す
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"signedUrl": signed_url})
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
