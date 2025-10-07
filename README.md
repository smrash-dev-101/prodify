# Prodify — Flask Microservice (DevOps Portfolio)

A tiny Flask API used to demonstrate a production-grade DevOps stack:
- Docker (multi-arch ready on Apple Silicon)
- GitHub Actions CI: test, scan, SBOM, sign, push to registry
- (Next) Terraform (AWS: VPC, EKS, ECR), Helm + Argo CD (GitOps)
- (Next) Observability (Prometheus/Grafana/Loki), SLOs & alerts

## API
- `GET /healthz` → `{"status":"ok"}`
- `GET /api/v1/hello` → `{"message":"Hello, world!"}` (set `HELLO_NAME` to override)

## Run locally (Python)
```bash
source .venv/bin/activate
python services/api/app.py
Run IN Docker                                                                                                                                                                                             cd services/api
docker buildx build --platform linux/amd64 -t prodify-api:dev --load .
docker run --rm -p 8000:8000 prodify-api:dev
# open http://localhost:8000/healthz
Structure                                                                                                                                                                                                 prodify/
  services/
    api/
      app.py
      requirements.txt
      Dockerfile
      .dockerignore
      tests/

## CI Status
![CI](https://github.com/smrash-dev-101/prodify/actions/workflows/ci.yml/badge.svg)
