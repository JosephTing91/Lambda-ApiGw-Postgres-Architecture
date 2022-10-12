variable "privsubnet3_id"{
}
variable "privsubnet4_id"{
}

variable "dbsg_id"{
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
  engine               = "MySQL"
  engine_version       = "8.0.30"
  instance_class       = "db.t2.micro"
  vpc_security_group_ids = [var.dbsg_id]
  db_subnet_group_name = aws_db_subnet_group.subnetgroup.name
  db_name               = "mydb"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
}

