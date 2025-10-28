import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
// Modelleri doğru yerlerinden import ediyoruz
import { Mulk } from '../models/mulk'; 
import { Musteri } from '../models/musteri'; 

@Injectable({
  providedIn: 'root'
})
export class PortfoyService {

  // **KRİTİK:** Backend API'nizin çalıştığı temel adres
  private apiUrl = 'http://localhost:8000/api'; 

  constructor(private http: HttpClient) { } 

  // Müşteri listesini çeken metot (Kaydet butonu testi için gerekli)
  getMusteriler(): Observable<Musteri[]> {
    return this.http.get<Musteri[]>(`${this.apiUrl}/musteriler/`);
  }

  // YENİ EKLENEN METOT: Mülk listesini çeken metot
  getMulkler(): Observable<Mulk[]> {
    // Django REST Framework'teki Mulk listeleme endpoint'i
    return this.http.get<Mulk[]>(`${this.apiUrl}/mulkler/`);
  }
}