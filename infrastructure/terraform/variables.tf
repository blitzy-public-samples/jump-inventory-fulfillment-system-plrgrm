# Project ID variable
variable "project_id" {
  description = "The Google Cloud Project ID"
  type        = string
}

# Region variable
variable "region" {
  description = "The Google Cloud region for resource deployment"
  type        = string
  default     = "us-central1"
}

# Environment variable
variable "environment" {
  description = "The deployment environment (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

# Database configuration variables
variable "database_instance_tier" {
  description = "The machine type for the database instance"
  type        = string
  default     = "db-f1-micro"
}

variable "database_name" {
  description = "The name of the database to create"
  type        = string
  default     = "myapp_db"
}

# Storage bucket configuration variables
variable "storage_bucket_name" {
  description = "The name of the Google Cloud Storage bucket"
  type        = string
}

variable "storage_bucket_location" {
  description = "The location for the Google Cloud Storage bucket"
  type        = string
  default     = "US"
}

# Cloud Run service configuration variables
variable "cloud_run_service_name" {
  description = "The name of the Cloud Run service"
  type        = string
}

variable "cloud_run_container_image" {
  description = "The container image to deploy to Cloud Run"
  type        = string
}

variable "cloud_run_service_account_email" {
  description = "The service account email for the Cloud Run service"
  type        = string
}

# Identity Platform configuration variables
variable "identity_platform_config" {
  description = "Configuration for Identity Platform"
  type = object({
    display_name             = string
    support_email            = string
    enable_email_link_signin = bool
  })
  default = {
    display_name             = "My App"
    support_email            = "support@myapp.com"
    enable_email_link_signin = true
  }
}

# Pub/Sub configuration variables
variable "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  type        = string
}

variable "pubsub_subscription_name" {
  description = "The name of the Pub/Sub subscription"
  type        = string
}

# Cloud Tasks configuration variables
variable "cloud_tasks_queue_name" {
  description = "The name of the Cloud Tasks queue"
  type        = string
}

variable "cloud_tasks_location" {
  description = "The location for the Cloud Tasks queue"
  type        = string
  default     = "us-central1"
}