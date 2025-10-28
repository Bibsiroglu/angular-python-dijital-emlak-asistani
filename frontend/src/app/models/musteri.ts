export interface Musteri {
    id: number; // Django'nun otomatik eklediği birincil anahtar
    ad_soyad: string;
    telefon: string;
    eposta: string | null; // Django'daki blank=True, null=True'ya karşılık gelir
    musteri_turu: 'ALICI' | 'SATICI' | 'KIRACI' | 'KİRACI'; // Django'daki choices seçeneklerine göre
    kayit_tarihi: string; // Tarih alanları genellikle string olarak gelir
    notlar: string | null;
}