terraform{
    required_providers {
        google ={
            source = "hashicorp/google"
            version = "4.9.0"
        }
        mongodbatlas = {
            source = "mongodb/mongodbatlas"
            version = "1.3.0"
        }
    }
}
provider "google" {
    project = "dice-arena-340310"
    credentials = var.credentials
    region = "europe-west1"
    zone = "europe-west1-b"
}

provider "mongodbatlas" {
    public_key = var.mongodbatlas_public_key
    private_key  = var.mongodbatlas_private_key
}

resource "google_compute_instance" "fraxaty" {
    machine_type = "e2-medium"
    name = "fraxaty-vm"
    boot_disk {
        initialize_params {
            image = "ubuntu-os-cloud/ubuntu-2004-lts"
            size = 50
        }
    }
    network_interface {
        network = google_compute_network.fraxaty_vpc.name
        access_config {
            nat_ip = "34.76.92.56"
        }
    }
    metadata = {
        ssh-keys = var.ssh_key
    }
}
output "public_ip" {
    value = google_compute_instance.fraxaty.network_interface[0].access_config[0].nat_ip
}
output "source_range" {
    value = google_compute_firewall.fraxaty-rule.source_ranges
}
resource "google_compute_network" "fraxaty_vpc" {
    name = "fraxaty-vpc"
}

resource "google_compute_firewall" "fraxaty-rule" {
    name = "fraxaty-firewall"
    network = "${google_compute_network.fraxaty_vpc.name}"
    allow {
        protocol = "icmp"
    }
    allow {
        protocol = "tcp"
        ports = ["22", "80", "8080", "90", "8020", "8000", "27017", "8081", "443"]
    }
    source_ranges = ["0.0.0.0/0"]
}

# resource "mongodbatlas_cluster" "da_cluster" {
#   project_id = "622713d2a6294122762effac"
#   name = "da_cluster"
#   cluster_type = "REPLICASET"
#   replication_specs {
#     num_shards = 1
#     regions_config {
#         region_name = "EUROPE_WEST"
#         electable_nodes = 3
#         priority = 7
#         read_only_nodes = 0
#     }
#   }
#   cloud_backup = true
#   auto_scaling_disk_gb_enabled = true
#   mongo_db_major_version = "4.2"
#   provider_name = "GCP"
#   disk_size_gb = 40
#   provider_instance_size_name = "M30"
# }