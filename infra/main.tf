terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "api_image" {
  name         = "meu-app-devops:v1"
  keep_locally = true
}

resource "docker_container" "api_container" {
  name  = "servidor-meu-app"
  image = docker_image.api_image.image_id

  ports {
    internal = 8000
    external = 9090
  }
}