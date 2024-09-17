# Main Terraform configuration file for provisioning Google Cloud resources

# Provider configuration for Google Cloud
provider "google" {
  project = var.project_id
  region  = var.region
}

# Resource definitions for Google Cloud SQL (PostgreSQL)
resource "google_sql_database_instance" "main" {
  name             = "main-instance"
  database_version = "POSTGRES_13"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }

  deletion_protection = false
}

resource "google_sql_database" "database" {
  name     = "main-database"
  instance = google_sql_database_instance.main.name
}

# Resource definitions for Google Cloud Storage buckets
resource "google_storage_bucket" "static_assets" {
  name     = "${var.project_id}-static-assets"
  location = var.region
}

resource "google_storage_bucket" "user_uploads" {
  name     = "${var.project_id}-user-uploads"
  location = var.region
}

# Resource definitions for Google Cloud Run services
resource "google_cloud_run_service" "web_app" {
  name     = "web-app"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/web-app:latest"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_cloud_run_service" "api_service" {
  name     = "api-service"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/api-service:latest"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Resource definitions for Google Cloud Identity Platform
resource "google_identity_platform_config" "default" {
  project = var.project_id
  
  # HUMAN ASSISTANCE NEEDED
  # Additional configuration for Identity Platform may be required
  # such as enabling specific authentication methods or configuring
  # custom domains. Please review and adjust as necessary.
}

# Resource definitions for Google Cloud Pub/Sub topics and subscriptions
resource "google_pubsub_topic" "main_topic" {
  name = "main-topic"
}

resource "google_pubsub_subscription" "main_subscription" {
  name  = "main-subscription"
  topic = google_pubsub_topic.main_topic.name

  ack_deadline_seconds = 20
}

# Resource definitions for Google Cloud Tasks queues
resource "google_cloud_tasks_queue" "default_queue" {
  name     = "default-queue"
  location = var.region

  rate_limits {
    max_dispatches_per_second = 10
    max_concurrent_dispatches = 10
  }

  retry_config {
    max_attempts = 5
  }
}