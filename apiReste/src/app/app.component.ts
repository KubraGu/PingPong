import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { JoueurComponent } from './joueur/joueur.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, JoueurComponent],
  templateUrl: './app.component.html',
})

export class AppComponent {
  title = 'PingPong';
}
