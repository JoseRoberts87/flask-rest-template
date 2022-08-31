# terraform {
#   backend "s3" {
#     bucket = ""
#   }
# }


provider "aws" {
  region = var.region
}
