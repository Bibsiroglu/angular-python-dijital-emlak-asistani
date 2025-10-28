export interface IstatistikVerisi {
    toplam_mulk: number;
    ortalama_fiyat: number;
    toplam_envanter_degeri: number;
    // Durum ve sayım ikililerini tutar (Örn: [{"durum": "KİRALIK", "sayi": 8}])
    durum_dagilimi: { durum: string; sayi: number }[]; 
}