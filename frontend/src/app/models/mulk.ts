export interface Mulk {
  id: number;
  baslik: string;
  durum: string;
  fiyat: number;
  sehir: string;
  ilce: string;
  brut_m2: number; 
  net_m2: number;
  oda_sayisi: string;
  bulundugu_kat?: number; 
  bina_kat_sayisi?: number; 
  adres: string;
  musteri_sahibi: number; // ForeignKey ID'si
  fotograflar: MulkFotografi[]; // Fotoğraflar için dizi
}

export interface MulkFotografi {
    foto: string; // Fotoğrafın URL'si
    aciklama: string;
}