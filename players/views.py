from django.shortcuts import render, redirect
from .models import Player
from django.contrib.auth.decorators import login_required
from . import forms


def players_list(request):
    players = Player.objects.all().order_by('short_name')
    return render(request, 'players/players_list.html', {'players': players})


def player_details(request, slug):
    player = Player.objects.get(slug=slug)
    if request.method == 'POST':
        comment_form = forms.AddComment(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.player = player
            new_comment.posted_by = request.user
            new_comment.save()
            return redirect('players:details', slug=slug)
    else:
        comment_form = forms.AddComment()
    return render(request, 'players/player_details.html', {'player': player, 'form': comment_form})


@login_required(login_url='/users/login/')
def add_player(request):
    if request.method == 'POST':
        form = forms.AddPlayer(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.added_by = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddPlayer()
    return render(request, 'players/add_player.html', {'form': form})

