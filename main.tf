terraform {
  cloud {
    organization = "OwlbearMedia"
    workspaces {
      name = "pepe-silvia-api"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.84.0"
    }
    # There is an issue with terraform where it can't find my docker daemon
    # however docker works fine for me locally.
    # @todo: debug this later
    # docker = {
    #   source  = "kreuzwerker/docker"
    #   version = "~> 3.0.2"
    # }
  }
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_lightsail_container_service" "pepe-silvia-api" {
  name        = "pepe-silvia-api"
  power       = "nano"
  scale       = 1
  is_disabled = false
}

# provider "docker" {}

# resource "docker_image" "flask-container" {
#   name         = "flask-container:latest"
#   keep_locally = false
# }

# resource "docker_container" "flask-container" {
#   image = docker_image.flask-container.image_id
#   name  = "flask-container"

#   ports {
#     internal = 5328
#     external = 5328
#   }
# }
