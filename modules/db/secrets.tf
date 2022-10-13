# variable "db_username"{
#   description = "Database administrator username"
#   type        = string
#   sensitive   = true
# }

# variable "db_password"{
#   description = "Database administrator password"
#   type        = string
#   sensitive   = true
# }

variable "sm_kms_arn"{}

resource "aws_kms_key" "secrets_kms_key"{
  description= "key for encrypting db secrets "

}

resource "aws_secretsmanager_secret" "secretmasterDB" {
name = "dbsecrets2"
kms_key_id=aws_kms_key.secrets_kms_key.arn
}

resource "aws_secretsmanager_secret_version" "sversion" {
secret_id = aws_secretsmanager_secret.secretmasterDB.id
secret_string = <<EOF
{"username": "${var.db_username}",
"password": "${var.db_password}",
  "host": "${aws_db_instance.default.address}"}
EOF
}


data "aws_secretsmanager_secret" "secretmasterDB" {
arn = aws_secretsmanager_secret.secretmasterDB.arn
}
data "aws_secretsmanager_secret_version" "creds" {
secret_id = data.aws_secretsmanager_secret.secretmasterDB.arn
}

output "db_secrets_arn"{
  value=aws_secretsmanager_secret.secretmasterDB.arn
}