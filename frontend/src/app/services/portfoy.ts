// src/app/services/portfoy.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Mulk } from '../models/mulk.interface'; // Mulk modelini import ediyoruz

@Injectable({
  providedIn: 'root'
})
export class PortfoyService {
  // Burayı kendi Django API'nizin ana adresiyle değiştirin
  private readonly API_URL = 'http://localhost:8000/api';

  constructor(private http: HttpClient) { }

  /**
   * Django API'den tüm mülk listesini çeker.
   * Django REST Framework (DRF) uç noktanızın '/api/mulkler/' olduğunu varsayıyoruz.
   */
  getMulks(): Observable<Mulk[]> {
    const url = `${this.API_URL}/mulkler/`;
    return this.http.get<Mulk[]>(url);
  }

  // İleride buraya 'getMusteriler', 'addMulk', 'updateMulk' vb. metotları ekleyebilirsiniz.
}