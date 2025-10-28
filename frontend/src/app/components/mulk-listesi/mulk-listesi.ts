import { Component, OnInit } from '@angular/core';
import { PortfoyService } from '../../services/portfoy';
import { Mulk } from '../../models/mulk'; // Güncel Mulk modelini import ediyoruz
import { CommonModule } from '@angular/common'; // ngFor, ngIf için
import { RouterModule } from '@angular/router'; // routerLink için

@Component({
  selector: 'app-mulk-listesi',
  standalone: true,
  imports: [CommonModule, RouterModule], 
  templateUrl: './mulk-listesi.html',
  styleUrl: './mulk-listesi.css' // Uzantınızın .css olduğundan emin olun
})
export class MulkListesiComponent implements OnInit {

  mulkler: Mulk[] = []; // Mülk verilerini tutacak dizi
  yukleniyor: boolean = true;
  hataMesaji: string | null = null;

  constructor(private portfoyService: PortfoyService) { }

  ngOnInit(): void {
    this.mulkleriGetir();
  }

  mulkleriGetir(): void {
    this.yukleniyor = true;
    this.hataMesaji = null;
    this.portfoyService.getMulkler().subscribe({
      next: (data) => {
        this.mulkler = data;
        this.yukleniyor = false;
      },
      error: (err) => {
        this.yukleniyor = false;
        console.error('Mulkler yuklenirken hata olustu:', err);
        this.hataMesaji = 'API baglantisi basarisiz. Backend sunucusunun calistigindan ve /api/mulkler/ endpointinin dogru oldugundan emin olun.';
      }
    });
  }

  // Para birimi formatlama metodu
  formatFiyat(fiyat: number): string {
    return new Intl.NumberFormat('tr-TR', { style: 'currency', currency: 'TRY' }).format(fiyat);
  }
}