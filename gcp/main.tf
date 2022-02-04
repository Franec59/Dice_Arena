terraform{
    required_providers {
        google ={
            source = "hashicorp/google"
            version = "4.9.0"
        }
    }
}

provider "google" {
    project = "dice-arena-340310"
    credentials = var.credentials
    region = "europe-west1"
    zone = "europe-west1-b"
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
            
        }
    }
    metadata = {
        ssh-keys = "thrawn.1809:${file("~/.ssh/id_rsa.pub")}"
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
        ports = ["22", "80"]
    }
    source_ranges = ["0.0.0.0/0"]
}
