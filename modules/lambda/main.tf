data "archive_file" "zip" {
    type        = "zip"
    source_file = "user_uploads.py"
    output_path = "user_uploads.zip" 

}


resource "aws_iam_role" "iam_for_app_lambda" {
  name = "iam_for_app_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
resource "aws_lambda_function" "app_lambda" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "${data.archive_file.zip.output_path}"
  function_name = "user_uploads"
  role          = aws_iam_role.iam_for_app_lambda.arn
  handler       = "user_uploads.lambda_handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = "${data.archive_file.zip.output_base64sha256}" 
  runtime = "python3.8"

  environment {
    variables = {
      foo = "bar"
    }
  }
}


#create lambda function to delete from table


data "archive_file" "zip_delete" {
    type        = "zip"
    source_file = "delete_function.py"
    output_path = "delete_function.zip" 

}


resource "aws_iam_role" "iam_for_delete_lambda" {
  name = "iam_for_delete_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
resource "aws_lambda_function" "delete_lambda" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "${data.archive_file.zip_delete.output_path}"
  function_name = "delete_function"
  role          = aws_iam_role.iam_for_delete_lambda.arn
  handler       = "delete_function.lambda_handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = "${data.archive_file.zip_delete.output_base64sha256}" 
  runtime = "python3.8"

  environment {
    variables = {
      foo = "bar"
    }
  }
}


