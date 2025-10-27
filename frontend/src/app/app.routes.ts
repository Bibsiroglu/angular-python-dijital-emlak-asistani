// src/app/app.routes.ts

import { Routes } from '@angular/router';
import { MulkListesiComponent } from './components/mulk-listesi/mulk-listesi'; 

export const routes: Routes = [
  // Ana Dizin (/) boş gelmemeli, varsayılan olarak Mulk Listesine yönlendirmeli
  { 
    path: '', 
    redirectTo: 'mulkler', 
    pathMatch: 'full' 
  },
  
  // Mülk Listesi Sayfası
  { 
    path: 'mulkler', 
    component: MulkListesiComponent 
  },

  
  // Bulunamayan tüm yollar için 404 sayfasına (veya ana sayfaya) yönlendirme
  { 
    path: '**', 
    redirectTo: 'mulkler' 
  }
];