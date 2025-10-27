
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app'; // <<< 'App' yerine 'AppComponent' kullanın
import { appConfig } from './app/app.config';

bootstrapApplication(AppComponent, appConfig).catch((err) =>
  console.error(err)
);