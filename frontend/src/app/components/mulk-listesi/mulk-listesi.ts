import { Component, OnInit } from '@angular/core';
import { PortfoyService } from '../../services/portfoy';
import { Mulk } from '../../models/mulk.interface'; 
import { catchError, of } from 'rxjs'; // Hata yakalamak için
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-mulk-listesi',
  standalone: true,
  imports: [CommonModule, MulkListesiComponent],
  templateUrl: './mulk-listesi.html',
  styleUrls: ['./mulk-listesi.css']
})
export class MulkListesiComponent implements OnInit {

  mulkler: Mulk[] = [];
  yukleniyor: boolean = true;
  hata: string | null = null;

  constructor(private portfoyService: PortfoyService) { }

  ngOnInit(): void {
    // Bileşen yüklendiğinde veriyi çek
    this.getMulks();
  }

  getMulks(): void {
    this.portfoyService.getMulks().subscribe({
      next: (data) => {
        this.mulkler = data;
        this.yukleniyor = false;
      },
      error: (err) => {
        // Hata yakalama
        this.hata = `Veri çekilirken bir hata oluştu. Lütfen CORS ayarlarını (Django) ve API adresini kontrol edin. Hata: ${err.statusText}`;
        this.yukleniyor = false;
        console.error('Veri çekme hatası:', err);
      }
    });
  }
}