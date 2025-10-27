import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MulkListesiComponent } from './components/mulk-listesi/mulk-listesi';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MulkListesiComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('emlak_asistani');
}
