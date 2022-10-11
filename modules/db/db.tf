variable "privsubnet3_id"{
}
variable "privsubnet4_id"{
}

variable "db_username"{
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "db_password"{
  description = "Database administrator password"
  type        = string
  sensitive   = true
}

resource "aws_db_subnet_group" "subnetgroup" {
  name       = "subnetgroup"
  subnet_ids = [var.privsubnet3_id, var.privsubnet4_id]
  tags = { Name = "My DB subnet group"}
}

resource "aws_db_instance" "default" {
  allocated_storage    = 10
  max_allocated_storage= 20
  engine               = "postgres"
  engine_version       = "10.17"
  instance_class       = "db.t2.micro"
  db_subnet_group_name = aws_db_subnet_group.subnetgroup.name
  db_name               = "postgresdb"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
}
