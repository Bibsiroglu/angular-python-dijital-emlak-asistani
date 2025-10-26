export type MulkTuru = 'KONUT' | 'ISYERI' | 'ARSA' | 'PROJE';
export type MulkDurumu = 'SATILIK' | 'KIRALIK' | 'SATILDI' | 'KIRALANDI' | 'PASIF';

export interface Mulk {
    id:number;
    baslik:string;
    aciklama:string;
    mulk_turu:MulkTuru;
    durum:MulkDurumu;
    
    fiyat:number;
    brut_m2:number | null;
    net_m2: number | null;
    oda_sayisi: string | null;

    adres:string;
    sehir:string;
    ilce:string;

    sahip: number | null;

    kayit_tarihi:string;
    güncelleme_tarihi:string;
}