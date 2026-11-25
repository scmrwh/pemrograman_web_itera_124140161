markdown
# RESTful API Manajemen Matakuliah & Mahasiswa — Pyramid

- **Nama Lengkap:** Suci Marwah Anissa
- **NIM:** 124140161
- **Kelas Praktikum:** RA 

## Deskripsi Aplikasi
Aplikasi RESTful API berbasis **Pyramid Framework** dan **PostgreSQL** untuk mengelola data **Mahasiswa** dan **Matakuliah**. Mengimplementasikan:
- Model data ORM (SQLAlchemy)
- Migrasi schema (Alembic)
- Routing URL Dispatch dengan predikat `request_method`
- View controller CRUD dengan renderer JSON

### Endpoint Matakuliah
| Method | URL | Keterangan |
|--------|-----|-----------|
| GET | `/api/matakuliah` | Menampilkan seluruh matakuliah |
| GET | `/api/matakuliah/{id}` | Detail matakuliah (404 jika tidak ada) |
| POST | `/api/matakuliah` | Tambah matakuliah (400 jika field tidak lengkap / sks·semester ≤ 0) |
| PUT | `/api/matakuliah/{id}` | Update matakuliah |
| DELETE | `/api/matakuliah/{id}` | Hapus matakuliah |

### Endpoint Mahasiswa
| Method | URL | Keterangan |
|--------|-----|-----------|
| GET | `/api/mahasiswa` | Menampilkan seluruh mahasiswa |
| GET | `/api/mahasiswa/{id}` | Detail mahasiswa |
| POST | `/api/mahasiswa` | Tambah mahasiswa |
| PUT | `/api/mahasiswa/{id}` | Update mahasiswa |
| DELETE | `/api/mahasiswa/{id}` | Hapus mahasiswa |

## Instalasi

### 1. Clone repositori
```bash
git clone https://github.com/<username>/pemrograman_web_itera_124140161.git
cd SuciMarwahAnissa_124140161_pertemuan6/pyramid_mahasiswa
```
### 2. Buat & aktifkan virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install --upgrade pip setuptools
pip install -e ".[testing]"
pip install psycopg2-binary
```
### 4. Setup database PostgreSQL
```sql
CREATE DATABASE pyramid_mahasiswa;
CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;
\c pyramid_mahasiswa
GRANT ALL ON SCHEMA public TO pyramid_user;
```

Edit development.ini:
```sql
sqlalchemy.url = postgresql+psycopg2://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa
```
### 5. Migrasi database
```bash
alembic -c development.ini upgrade head
```
### 6. Seeding data awal
```bash
python -m pyramid_mahasiswa.scripts.initialize_db development.ini
```
### 7. Jalankan server
```bash
pserve development.ini --reload
Server jalan di http://localhost:6543.
```


## Bukti Pengujian (Screenshot)

### GET /api/matakuliah
![GET all matakuliah](docs/1.png)

### GET /api/matakuliah/1
![GET detail matakuliah](docs/2.png)

### POST /api/matakuliah
![POST matakuliah](docs/3.png)

### POST Validasi Field Kurang (400)
![POST 400 field](docs/4.png)

### POST Validasi sks ≤ 0 (400)
![POST 400 sks](docs/5.png)

### PUT /api/matakuliah/1
![PUT matakuliah](docs/6.png)

### DELETE /api/matakuliah/3
![DELETE matakuliah](docs/7.png)

### GET 404 (ID terhapus)
![GET 404](docs/8.png)

### GET /api/mahasiswa (endpoint lama)
![GET mahasiswa](docs/9.png)