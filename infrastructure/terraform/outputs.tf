output "database_connection_string" {
  description = "Connection string for the Cloud SQL database"
  value       = google_sql_database_instance.main.connection_name
  sensitive   = true
}

output "storage_bucket_urls" {
  description = "URLs for the created Cloud Storage buckets"
  value = {
    media_bucket = google_storage_bucket.media.url
    backup_bucket = google_storage_bucket.backup.url
  }
}

output "cloud_run_service_urls" {
  description = "URLs for the deployed Cloud Run services"
  value = {
    api_service = google_cloud_run_service.api.status[0].url
    web_service = google_cloud_run_service.web.status[0].url
  }
}

output "identity_platform_config" {
  description = "Configuration details for Identity Platform"
  value = {
    project_id = google_identity_platform_config.main.project
    api_key    = google_identity_platform_config.main.api_key
  }
  sensitive = true
}

output "pubsub_resources" {
  description = "IDs for created Pub/Sub topics and subscriptions"
  value = {
    topics = {
      for topic in google_pubsub_topic.topics : topic.name => topic.id
    }
    subscriptions = {
      for sub in google_pubsub_subscription.subscriptions : sub.name => sub.id
    }
  }
}

output "cloud_tasks_queues" {
  description = "Names of the created Cloud Tasks queues"
  value = [for queue in google_cloud_tasks_queue.queues : queue.name]
}

# HUMAN ASSISTANCE NEEDED
# Please review the outputs to ensure all necessary information is included
# and that sensitive information is properly marked as sensitive.
# Additional outputs may be required based on the specific resources created in the Terraform configuration.