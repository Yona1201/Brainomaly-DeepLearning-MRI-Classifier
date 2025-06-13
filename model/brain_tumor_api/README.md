# Brain Tumor Classification API (FastAPI)

## Cara Menjalankan

1.  **Install dependensi**
pip install  -r  requirements.txt 

2. **Jalankan  API**
uvicorn main:app  --reload

3. **Buka  browser  Akses**
http://localhost:8000/docs

4. Upload  Gambar  MRI
Di  situ  kamu  bisa:
- Klik  endpoint  /predict
- Upload  file  gambar  MRI
- Klik  “Execute”
- Lihat  hasil  prediksi

Hasil prediksi  akan  muncul  di  bagian  bawah:
label: jenis  tumor (misalnya: Glioma,  No  Tumor,  dll)
confidence: seberapa  yakin  modelnya
class_id: indeks  kelas

Jika ingin melihat link deploy Railway 
https://brain-tumor-api.up.railway.app/