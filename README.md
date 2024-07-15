# **Marketplace Reviews Prediction**

![workflow status](https://github.com/luthfanali/marketplace-reviews/actions/workflows/ci.yaml/badge.svg)
![workflow status](https://github.com/luthfanali/marketplace-reviews/actions/workflows/cd-staging.yaml/badge.svg)
![workflow status](https://github.com/luthfanali/marketplace-reviews/actions/workflows/cd-push-registry.yaml/badge.svg)

## Dataset dan Model

Dataset yang digunakan dalam project kali ini adalah dataset dari kaggle: [Dataset Review Tokopedia dan Shopee](https://www.kaggle.com/datasets/silviamargareta/dataset-review)

- Unduh dataset tersebut
- Rename `CSV` menjadi `marketplace-reviews.csv`
- Masukkan dalam folder `notebooks/data/`

## Setup Infrasucture di AWS

### Instance #1: Tracking Infrastructure
- Setup pada VPS sendiri
- Copy ke dalam server seluruh file `others/docker-engine`
- Jalankan setup Docker `install-docker-engine.sh`
- Masuk ke folder `others/docker-engine/platforms` dan lakukan

    ```
    docker compose up --build --detach
    ```
    ![Proses Instalasi](./others/img/instalasi_platform.png)
- MinIO, MLFlow, dan Postgress telah berjalan 

    ![Platform sudah berjalan](./others/img/image_sudah_berjalan.png)
- Buat database baru bernama `marketplace_reviews` di Postgress

### Instance #2
- Setup server AWS, t3a micro.
- Generate SSH Key, lalu tambahkan public key ke dalam Github Key
- Install docker di dalamnya

### Instance #3
- Setup server AWS, t3a micro.
- Generate SSH Key, lalu tambahkan public key ke dalam Github Key
- Install docker di dalamnya


## Setup Repository
- Buat repository baru di local computer. Repo ini bertujuan untuk jadi Template Machine Learning Project kita kedepannya
- Pada halaman Github, buat sebuah repo baru. 
- Kemudian di halaman Settings repo tersebut centang opsi `Template Repository` 

    ![Centang Template Repository](./others/img/template_repo.png)
- Setelah selesai menyiapkan template project, lakukan `git push` 

## Setup Local Environment
- Buat repository baru bernama `marketplace-reviews` dengan memakai template [ML Project Template](https://github.com/luthfanali/ml-project-template)
- Clone ke dalam local computer dengan command 
    ```
    git clone git@github.com:luthfanali/marketplace-reviews.git
    ```
- Pada direktori project buat sebuah python environment baru dengan mengetik 
    ```
    python -m venv .marketplace-reviews-venv
    ```
- Kemudian instalasi semua dependensi python yang diperlukan dengan 
    ```
    pip install -r requirements.txt
    ```
- Edit project

- Pada MinIO, buat sebuah bucket baru dengan nama `marketplace-reviews-bucket`

- Buat DVC Pipeline
  - Inisialisasi DVC
    ```
    dvc init
    ```
  - Buat file `dvc.yaml` di project root directory, kemudian edit sesuai kebutuhan
  - Repro DVC
    ```
    dvc repro
    ```
  - Update DVC Configuration
    1.  Tambah bucket di MinIO ke dalam DVC
        ```
        dvc remote add -d storage s3://marketplace-reviews-dvc-pipeline-bucket
        ```
    2. Tambah Endpoint URL
        ```
        dvc remote modify storage endpointurl http://localhost:9000
        ```
    3. Masukkan Access Key ID Minio
        ```
        dvc remote modify storage access_key_id <akses_key_minio>
        ```
    4. Masukkan Secret Key MinIO
        ```
        dvc remote modify storage secret_access_key <secret_key_minio>
        ```
  - Push ke server dengan `dvc push`
  
- Commit seluruh perubahan
- Lakukan Push ke Github

## Experimenting, Evaluating and Comparing Models
- Repository sudah tersetup workflownya
- Dilakukan adjustment pada parameter model, dengan mengganti `MAX_ITER` dari 300 menjadi 100
- Diperoleh hasil seperti di bawah ini 

    ![Hasil model](./others/img/perbandingan_model.png)

- Pilih model yang terbaik, lalu tambahkan alias `development` dan `staging`

## Setup CI/CD

### Integrasi CI
- Buat branch baru
  
  ```
  git checkout -b feat/enable-ci-unittest
  ``` 
- Buat pipeline untuk CI berupa `ci.yaml` dan masukkan dalam `.github/workflows`
- Commit perubahan dalam branch `feat/enable-ci-unittest`
- Lalu push ke Github
- Lakukan Pull Request
- Tunggu hingga proses testing selesai
  
  ![Proses CI unit test](./others/img/proses_ci.png)

- Lakukan merge apabila testing berhasil
  
  ![Proses CI berhasil](./others/img/ci_berhasil.png)

### Integrasi CD
- Buat branch baru
  
  ```
  git checkout -b feat/enable-cd-staging
  ``` 
- Buat pipeline untuk CD berupa `cd-staging.yaml` dan masukkan dalam `.github/workflows`
- Commit perubahan dalam branch `feat/enable-cd-staging`
- Lalu push ke Github
- Pada pengaturan repository, tambahkan **Secret** dan **Vars** yang dibutuhkan sesuai dengan pipeline `cd-staging.yaml`
- Lakukan Pull Request
- Tunggu hingga proses testing dan deploying selesai
  
  ![Sukses terdeploy ke STG Server](./others/img/sukses_deploy_ke_stg.png)
- Coba lakukan test API ke Server Staging
  
  ![Sukses hit API ke STG](./others/img/sukses_hit_API.png)
