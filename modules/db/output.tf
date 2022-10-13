
output "db_endpoint" {
    value = aws_db_instance.default.endpoint
}

output "db_pass_arn" {
    value=aws_ssm_parameter.db_password.arn
}
output "db_user_arn" {
    value=aws_ssm_parameter.db_username.arn
}
output "db_endpoint_arn" {
    value=aws_ssm_parameter.db_endpoint.arn
}

output "secret_kms_keyId"{
  value=aws_kms_key.secrets_kms_key.key_id

}

output "secret_kms_keyArn"{
  value=aws_kms_key.secrets_kms_key.arn

}
