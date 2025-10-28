import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
// Navbar'ı import edin
import { NavbarComponent } from './components/navbar/navbar'; 

@Component({
  selector: 'app-root',
  standalone: true,
  // NavbarComponent'i imports dizisine ekliyoruz
  imports: [RouterOutlet, NavbarComponent], 
  templateUrl: './app.html', // Veya template: '...'
  styleUrl: './app.css'
})
export class AppComponent {
  title = 'Emlak Asistani'; 
}