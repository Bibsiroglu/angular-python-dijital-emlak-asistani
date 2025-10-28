import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
// Diğer modeller
import { Mulk } from '../models/mulk'; 
import { Musteri } from '../models/musteri'; 
// YENİ IMPORT: IstatistikVerisi'ni ayrı model dosyasından çekiyoruz
import { IstatistikVerisi } from '../models/istatistik.interface'; 

@Injectable({
  providedIn: 'root'
})
export class PortfoyService {

  private apiUrl = 'http://localhost:8000/api'; 

  constructor(private http: HttpClient) { } 

  // Mevcut metotlar
  getMusteriler(): Observable<Musteri[]> {
    return this.http.get<Musteri[]>(`${this.apiUrl}/musteriler/`);
  }

  getMulkler(): Observable<Mulk[]> {
    return this.http.get<Mulk[]>(`${this.apiUrl}/mulkler/`);
  }
  
  // YENİ METOT
  getIstatistikler(): Observable<IstatistikVerisi> {
      // Artık IstatistikVerisi tipini kullanıyoruz
      return this.http.get<IstatistikVerisi>(`${this.apiUrl}/istatistikler/`);
  }
}