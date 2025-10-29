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
