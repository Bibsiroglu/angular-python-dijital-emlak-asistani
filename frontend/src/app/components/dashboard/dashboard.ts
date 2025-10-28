import { Component, OnInit } from '@angular/core';
// Gerekli Angular modülleri
import { CommonModule, CurrencyPipe } from '@angular/common'; // NgIf, NgFor ve Pipe'lar için
import { RouterLink } from '@angular/router'; // Yönlendirme için (Navigasyon Menüsü veya Linkler)

// Servis ve Modeller
import { PortfoyService } from '../../services/portfoy';
import { IstatistikVerisi } from '../../models/istatistik.interface'; // Yeni, ayrı modelden import

@Component({
  selector: 'app-dashboard',
  // Projeniz büyük ihtimalle standalone component yapısını kullanıyor.
  // Eğer kullanmıyorsa 'standalone: true' ve 'imports' satırlarını kaldırıp
  // AppModule'a eklemeniz gerekir.
  standalone: true, 
  imports: [
    CommonModule, 
    RouterLink,
    // Angular'ın CurrencyPipe'ını kullanmak için imports'a ekliyoruz
    CurrencyPipe
  ], 
  
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {
  
  /** Django API'sinden çekilen istatistik verisini tutar. */
  istatistikler: IstatistikVerisi | undefined;
  
  /** Verilerin yüklenip yüklenmediğini kontrol eder. */
  isLoading = true;
  
  /** Hata mesajlarını tutar */
  errorMessage: string | null = null;

  constructor(private portfoyService: PortfoyService) { }

  ngOnInit(): void {
    this.getDashboardVerileri();
  }

  /**
   * PortfoyService üzerinden istatistik verilerini çeken metot.
   */
  getDashboardVerileri(): void {
    this.isLoading = true;
    this.errorMessage = null;

    this.portfoyService.getIstatistikler().subscribe({
      next: (data) => {
        // Veri başarıyla çekildi
        this.istatistikler = data;
        this.isLoading = false;
        console.log("Dashboard Verileri Başarıyla Yüklendi:", data);
      },
      error: (err) => {
        // Hata durumunda yüklenme durumunu kapat ve hatayı göster
        this.isLoading = false;
        this.istatistikler = undefined; 

        if (err.status === 0) {
            this.errorMessage = "Django sunucusuna ulaşılamadı. Lütfen sunucunun çalışıp çalışmadığını kontrol edin.";
        } else {
            this.errorMessage = "Veri yüklenirken bir hata oluştu: " + (err.message || 'Bilinmeyen Hata');
        }
        console.error("Dashboard verileri yüklenirken hata oluştu:", err);
      }
    });
  }

}