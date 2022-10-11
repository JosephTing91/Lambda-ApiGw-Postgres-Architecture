variable "vpc_id"{
}

variable "cidr_blocks"{
}



resource "aws_security_group" "DB-SG" {
  name        = "DB sg"
  description = "Allow 5432"
  vpc_id      = var.vpc_id
  ingress {
    description      = "DB SG"
    from_port        = 5432
    to_port          = 5432
    protocol         = "tcp"
    cidr_blocks      = [var.cidr_blocks["vpc"]]

  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "DB sg"
  }
}



resource "aws_security_group" "sg_lambda" {
  name        = "Lambda sg"
  vpc_id      = var.vpc_id

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
    tags = {
    Name = "Lambda sg"
  }
}


resource "aws_security_group_rule" "lambda_rds" {
  type                      = "ingress"
  from_port                 = 5432
  to_port                   = 5432
  protocol                  = "tcp"

  security_group_id         = aws_security_group.DB-SG.id
  source_security_group_id  = aws_security_group.sg_lambda.id
}

