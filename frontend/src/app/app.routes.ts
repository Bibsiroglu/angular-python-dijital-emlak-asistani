import { Routes } from '@angular/router';

import { MulkListesiComponent } from './components/mulk-listesi/mulk-listesi'; 
import { MulkEkle } from './components/mulk-ekle/mulk-ekle'; 

export const routes: Routes = [
  { 
    path: '', 
    redirectTo: 'mulkler', 
    pathMatch: 'full' 
  },
  { 
    path: 'mulkler', 
    component: MulkListesiComponent
  },

];