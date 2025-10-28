import { Routes } from '@angular/router';

import { DashboardComponent } from './components/dashboard/dashboard'; 
import { MulkListesiComponent } from './components/mulk-listesi/mulk-listesi'; 


export const routes: Routes = [
    
    // 1. ANA ROTA DEĞİŞİKLİĞİ: 
    // Uygulama açıldığında (URL: /) artık Mülk Listesi'ni göster.
    { 
        path: '', 
        component: MulkListesiComponent, // <-- DEĞİŞTİ! Dashboard yerine Liste
        title: 'Mülk Listesi'
    },
    
    // 2. Dashboard Rotası (Yeni, açık bir yola taşıdık)
    { 
        path: 'dashboard', // <-- YENİ YOL
        component: DashboardComponent,
        title: 'Yönetim Paneli'
    },
    
    // Mülk Listesi rotası (Kaldırıldı, artık ana rota tarafından karşılanıyor)
    // Eğer "/mulkler" yoluyla da erişilmesini istiyorsanız aşağıdaki satırı koruyabilirsiniz:
    // { path: 'mulkler', component: MulkListesiComponent, title: 'Mülk Listesi' },
    
    
    // Tanımsız rotayı ana sayfaya yönlendir (Mülk Listesi)
    { 
        path: '**', 
        redirectTo: '' 
    }
];