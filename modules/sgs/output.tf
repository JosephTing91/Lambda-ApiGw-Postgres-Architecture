output "sg_id_lambda" {
    value = aws_security_group.sg_lambda.id
}

# output "sg_id_default" {
#     value = aws_default_security_group.sg_default.id
# }


output "dbsg_id" {
    value=aws_security_group.DB-SG.id 

}
