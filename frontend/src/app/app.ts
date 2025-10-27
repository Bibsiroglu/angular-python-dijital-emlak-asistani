import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router'; // RouterOutlet import'u kalmalı

// MulkListesiComponent'i buradan çıkardık, çünkü RouterOutlet onu yönetecek.
// import { MulkListesiComponent } from './components/mulk-listesi/mulk-listesi.ts'; 

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.html',
  styleUrls: ['./app.css'],
  
  // SADECE ROUTEROUTLET'İ TUTUN (veya tüm modülleri)
  imports: [RouterOutlet], 
})
export class AppComponent {
  title = 'emlak-ui';
}