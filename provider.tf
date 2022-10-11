provider "aws" {
  region                   = "us-east-1"
  profile                  = "default"
  shared_credentials_files = ["C:/Users/Maitri WInd/.aws/credentials"]
}

provider "aws" {
  region                   = "us-east-1"
  profile                  = "awstest19"
  alias                    = "awstest19"
  shared_credentials_files = ["C:/Users/Maitri WInd/.aws/credentialstest19"]
}

