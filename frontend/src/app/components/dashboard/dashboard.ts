import { Component, OnInit } from '@angular/core';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { RouterLink } from '@angular/router';

// Servis ve Modeller
import { PortfoyService } from '../../services/portfoy';
import { IstatistikVerisi } from '../../models/istatistik.interface'; 

// === KRİTİK GRAFİK IMPORTLARI VE KAYIT ===
// Chart.js tiplerini doğru import ediyoruz
import { ChartConfiguration, ChartOptions, ChartType, ChartData, TooltipItem, Chart, registerables } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts'; 

// KRİTİK: "doughnut is not a registered controller" hatasını çözmek için
Chart.register(...registerables); 
// =========================================

@Component({
  selector: 'app-dashboard',
  standalone: true, 
  imports: [
    CommonModule, 
    RouterLink,
    CurrencyPipe,
    BaseChartDirective // Grafik bileşenini imports'a ekliyoruz
  ], 
  // Lütfen dosya adınızın 'dashboard.html' veya 'dashboard.component.html' olduğundan emin olun.
  templateUrl: './dashboard.html', 
  styleUrls: ['./dashboard.css'] 
})
export class DashboardComponent implements OnInit {
  
  istatistikler: IstatistikVerisi | undefined;
  isLoading = true;
  errorMessage: string | null = null;

  // === GRAFİK DEĞİŞKENLERİ: TİPLENDİRME DÜZELTİLDİ ===
  public durumDagilimiChartData: ChartData<'doughnut', number[], string> = {
      labels: [], 
      datasets: [ 
          { data: [], label: 'Mülk Durumu' } 
      ]
  };
  
  public durumDagilimiChartOptions: ChartOptions<'doughnut'> = {
    responsive: true,
    maintainAspectRatio: false, 
    plugins: {
      legend: { position: 'top' },
      tooltip: {
        callbacks: {
          label: (context: TooltipItem<'doughnut'>) => { 
            const label = context.label || '';
            const value = context.parsed;
            return `${label}: ${value} Adet`;
          },
        },
      },
    },
  };
  
  // HATA ÇÖZÜMÜ: TS2322 hatası için kesin string literal tipi kullanılır.
  public durumDagilimiChartType: 'doughnut' = 'doughnut'; 
  // =================================================

  constructor(private portfoyService: PortfoyService) { }

  ngOnInit(): void {
    this.getDashboardVerileri();
  }

  getDashboardVerileri(): void {
    this.isLoading = true;
    this.errorMessage = null;

    this.portfoyService.getIstatistikler().subscribe({
      next: (data) => {
        this.istatistikler = data;
        this.isLoading = false;
        this.prepareDurumDagilimiChartData(data.durum_dagilimi); 
      },
      error: (err) => {
        this.isLoading = false;
        this.istatistikler = undefined; 
        if (err.status === 0) {
            this.errorMessage = "Django sunucusuna ulaşılamadı. Lütfen sunucunun çalışıp çalışmadığını kontrol edin.";
        } else {
            this.errorMessage = "Veri yüklenirken bir hata oluştu: " + (err.message || 'Bilinmeyen Hata');
        }
      }
    });
  }

  private prepareDurumDagilimiChartData(dagilim: { durum: string; sayi: number }[]): void {
    const labels: string[] = [];
    const data: number[] = [];
    
    dagilim.forEach(item => {
      labels.push(item.durum);
      data.push(item.sayi);
    });

    this.durumDagilimiChartData = { 
        labels: labels,
        datasets: [{ 
            data: data, 
            label: 'Mülk Durumu', 
            // Basit renk dizisi
            backgroundColor: ['#007bff', '#28a745', '#ffc107', '#dc3545', '#17a2b8', '#6610f2']
        }]
    };
  }
}