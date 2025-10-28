// src/app/app.routes.ts

import { Routes } from '@angular/router';

import { MulkListesi } from './components/mulk-listesi/mulk-listesi'; 
import { MulkEkle } from './components/mulk-ekle/mulk-ekle'; 

export const routes: Routes = [
  { 
    path: '', 
    redirectTo: 'mulkler', 
    pathMatch: 'full' 
  },
  { 
    path: 'mulkler', 
    component: MulkListesi
  },
  { 
    path: 'mulk-ekle', 
    component: MulkEkle
  },
  { 
    path: '**', 
    redirectTo: 'mulkler' 
  }
];