from kubernetes import client, config
import subprocess

cpus = ["2-3", "4-5", "6-7"]

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()

def pincpu_pod(pod, cpu):
    for container in pod.spec.containers:
        pincpu_container(container.name, cpu)

def pincpu_container(containername, cpu):
    bashCommand = "runc --root=/var/run/containerd/runc/k8s.io update --cpuset-cpus {} {}".format(cpu, containername)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def create_load(cpu):
    pods = v1.list_namespaced_pod(namespace="")

    bashCommand = "./load_generator"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    pods_new = v1.list_namespaced_pod(namespace="")

    created_pods = pods_new.items - pods.items

    for pod in created_pods:
        pincpu_pod(pod, cpu)


if __name__=="__main__":
    for cpu in cpus:
        create_load(cpu)