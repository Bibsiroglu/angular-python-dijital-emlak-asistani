// media/js/toggle_mulk_tipleri.js
document.addEventListener('DOMContentLoaded', function() {
    // 1. Gerekli HTML Elementlerini Seçme
    
    // a) Mülk Türü (SELECT) alanı. Django Admin'de ID'si 'id_' ile başlar.
    const mulkTuruSelect = document.getElementById('id_mülk_turu');
    
    // b) Konut Tipi alanının satırı (div.form-row'u)
    // Django Admin her alan için bir .form-row oluşturur.
    const konutTipiRow = document.getElementById('id_konut_tipi').closest('.form-row');
    
    // c) İşyeri Tipi alanının satırı
    const isyeriTipiRow = document.getElementById('id_isyeri_tipi').closest('.form-row');

    // Eğer gerekli elementler sayfada yoksa (farklı bir model sayfası olabilir), işlemi durdur.
    if (!mulkTuruSelect || !konutTipiRow || !isyeriTipiRow) {
        return;
    }

    // 2. Alanların Görünürlüğünü Ayarlayan Ana Fonksiyon
    function toggleFieldVisibility() {
        const selectedValue = mulkTuruSelect.value;
        
        // KONUT seçilmişse: Konut Tipini göster, İşyeri Tipini gizle
        if (selectedValue === 'KONUT') {
            konutTipiRow.style.display = 'flex'; // veya 'block' veya 'table-row' (Admin yapısına göre değişir)
            isyeriTipiRow.style.display = 'none';
        } 
        // ISYERI seçilmişse: İşyeri Tipini göster, Konut Tipini gizle
        else if (selectedValue === 'ISYERI') {
            konutTipiRow.style.display = 'none';
            isyeriTipiRow.style.display = 'flex';
        } 
        // Başka bir şey seçilmişse (ARSA, PROJE vb.): İkisini de gizle
        else {
            konutTipiRow.style.display = 'none';
            isyeriTipiRow.style.display = 'none';
        }
    }

    // 3. Olay Dinleyicilerini Ekleme
    
    // Değer değiştiğinde görünürlüğü ayarla
    mulkTuruSelect.addEventListener('change', toggleFieldVisibility);

    // Sayfa ilk yüklendiğinde de görünürlüğü ayarla (Mulk düzenlenirken mevcut değeri korumak için)
    toggleFieldVisibility();
});
