export type MusteriTuru = 'ALICI'| 'SATICI' | 'KIRACI' | 'KIRALAYAN' | 'YATIRIMCI'

export interface Musteri {
    id: number;
    ad_soyad: string;
    telefon:string;
    eposta:string | null; // Django'da null=True olduğu için null olabilir.
    musteri_turu:MusteriTuru
    kayıt_tarihi:string; //Tarih saat bilgisi genellikle string olarak gelir.
    notlar:string;
}