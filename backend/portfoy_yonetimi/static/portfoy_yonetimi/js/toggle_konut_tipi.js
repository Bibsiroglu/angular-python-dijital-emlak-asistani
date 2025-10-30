<<<<<<< HEAD
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
=======
(function() { 
    // Tüm sayfa ve scriptler yüklendikten sonra çalışmayı garanti eden event listener
    window.addEventListener('load', function() {
        
        // 1. KRİTİK KONTROL: django.jQuery'nin gerçekten var olup olmadığını kontrol et
        if (typeof django === 'undefined' || typeof django.jQuery === 'undefined') {
            console.error("KRİTİK HATA: django.jQuery yüklenmedi. Admin paneli düzgün yüklenmiyor olabilir.");
            return;
        }

        // KRİTİK DÜZELTME: django.jQuery'i yerel $ takma adına ata
        var $ = django.jQuery; 
        
        console.log("toggle_konut_tipi.js çalışıyor ve jQuery başarıyla yüklendi.");

        // ----------------------------------------------------
        // 2. Fonksiyonel Kod Bloğu
        // ----------------------------------------------------

        // Mülk Türü SELECT elementini name özelliğine göre bul (En güvenli çözüm)
        // [name="mülk_turu"] seçicisi, Türkçe karakterli name'ler için en güvenilir yoldur.
        var propertyTypeSelector = $('[name="mülk_turu"]'); 
        
        // Konut Tipi alanının kapsayıcısını bulma (.field-konut_tipi Admin sınıfını kullanıyoruz)
        var konutTipiRow = $('.field-konut_tipi'); 
        
        // Eğer Mülk Türü elementi bulunamazsa
        if (propertyTypeSelector.length === 0) {
            console.error("HATA: Mülk Türü elementi (name='mülk_turu') bulunamadı! Lütfen HTML name değerini kontrol edin.");
            return;
        }
        
        // Alanın görünürlüğünü yöneten ana fonksiyon
        function toggleKonutTipi(selectedValue) {
            console.log("Seçilen Mülk Türü:", selectedValue);
            
            if (konutTipiRow.length === 0) {
                 console.error("HATA: Gizlenecek/Gösterilecek 'Konut Tipi' alanı (class .field-konut_tipi) bulunamadı! Alanı gizleyemiyoruz.");
            }
            
            // Seçilen değer 'KONUT' ise göster, değilse gizle.
            if (selectedValue === 'KONUT') { 
                konutTipiRow.show();
                console.log("-> KONUT seçildi. Konut Tipi gösterildi.");
            } else {
                konutTipiRow.hide();
                console.log("-> Başka tür seçildi. Konut Tipi gizlendi.");
            }
        }
        
        // 1. Sayfa ilk yüklendiğinde ayarla
        var initialValue = propertyTypeSelector.val();
        toggleKonutTipi(initialValue);
        
        // 2. Mülk Türü değiştiğinde fonksiyonu tekrar çalıştır
        propertyTypeSelector.change(function() {
            toggleKonutTipi($(this).val());
        });
    });
})(); 
>>>>>>> a1f25bef153a3963e887b33ac4d29395bc21cba0
