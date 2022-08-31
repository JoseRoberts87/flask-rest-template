output "hosted_at" {
  description = "The hosted at URL"
  value       = module.single_page_app_cloudfront.domain_name
}
