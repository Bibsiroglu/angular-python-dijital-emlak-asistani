import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 
// KRİTİK: Router özelliklerini tanımak için bu importlar gereklidir!
import { RouterLink, RouterLinkActive } from '@angular/router'; 

@Component({
  selector: 'app-navbar',
  standalone: true,
  // DÜZELTME: RouterLink ve RouterLinkActive'i imports'a ekliyoruz
  imports: [CommonModule, RouterLink, RouterLinkActive], 
  // UYARI: template yolunu düzeltin
  templateUrl: './navbar.html', 
  styleUrl: './navbar.css'
})
export class NavbarComponent {
}