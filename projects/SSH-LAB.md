# SSH Lab — Keys, Remote Hosts, and Jump Hosts

**Level:** Beginner-friendly, but this is a *real* infrastructure skill — the same one professional engineers use every day to reach servers.
**Time:** about 1.5–2 hours, and you can split it across sittings.
**What you need:** a Mac, the Terminal app, an internet connection, and patience with the occasional error message (errors are normal here — there's a troubleshooting section at the end).

---

## What you'll be able to do when you're done

- Explain what an SSH key pair is and why it's safe.
- Generate your own key pair.
- Create one or more real Linux "remote hosts" on your own laptop.
- Log into them securely with your key — no passwords.
- Set up short names so you can type `ssh host1` instead of a long command.
- Reach a "locked-down" server by *jumping through* a gateway host — the exact pattern used to reach protected production machines.

Work top to bottom. Don't skip the **Understand this** boxes or the **Checkpoints** — those are the difference between copying commands and actually learning.

---

## The one idea to hold onto: public vs. private keys

Before any commands, get this mental model, because everything else rests on it.

An SSH **key pair** is two matching files:

- A **private key** — secret, stays on your laptop, *never leaves it, never gets shared with anyone, ever.*
- A **public key** — safe to hand out. You copy this onto any server you want to log into.

They're mathematically linked. A server that has your **public** key can verify that you hold the matching **private** key, without ever seeing the private one. That's how you log in with no password: the server challenges you, your laptop answers using the private key, and the math checks out.

> **Understand this:** think of the public key as a padlock you can hand to anyone, and the private key as the only key that opens it. You can mail padlocks all over the world; as long as you keep the key, nobody can get in. If you ever remember only one rule from this lab: **never share or copy your private key anywhere.**

---

## Part 0 — Warm-up: SSH into your own Mac (5–10 minutes)

Your Mac can act as its own practice "server." This lets you complete a full key-based login before installing anything.

### 0.1 — Open the Terminal

Press `Cmd + Space`, type `Terminal`, hit Enter. This black window is a **shell** — a place to type commands instead of clicking. Find out your username by running:

```
whoami
```

Write that name down — you'll use it in a moment.

### 0.2 — Turn on the SSH server

Go to **System Settings → General → Sharing**, and switch **Remote Login** on. That starts the SSH server built into macOS.

### 0.3 — Generate your key pair

Run this (put your own email or a label in the quotes):

```
ssh-keygen -t ed25519 -C "your-name-ssh-lab"
```

- When it asks *where* to save, just press Enter to accept the default (`~/.ssh/id_ed25519`).
- When it asks for a **passphrase**, you can press Enter twice for none while you're learning. (A passphrase is an extra password protecting the private key itself — good practice for real life, covered in the stretch goals.)

Now look at what you made:

```
ls -l ~/.ssh
```

You should see two new files: `id_ed25519` (the **private** key — secret) and `id_ed25519.pub` (the **public** key — shareable). Peek at the public one:

```
cat ~/.ssh/id_ed25519.pub
```

That single line starting with `ssh-ed25519` is your padlock. Do **not** `cat` the other file and paste it anywhere.

### 0.4 — Authorize your key and connect

Tell your Mac to trust that key, then log in to yourself:

```
ssh-copy-id your-username@localhost
```

(Type your real username from step 0.1. It'll ask for your Mac password once — that's expected.)

Now connect:

```
ssh your-username@localhost
```

The first time, it'll warn about an unknown "fingerprint" and ask if you're sure — type `yes`. You're now in an SSH session *to your own machine*. Type `exit` to leave.

> **Understand this:** `ssh-copy-id` just appended your public key to a file called `~/.ssh/authorized_keys` on the server. That file is the guest list — any public key in it is allowed in. You'll do this by hand on the next part so you see exactly how it works.

**✅ Checkpoint 0:** In your own words, why was it safe to copy your public key onto the server, but it would *not* be safe to copy your private key? Say it out loud before moving on.

---

## Part 1 — Real remote hosts with Multipass (the main event)

Logging into your own Mac is training wheels. Now you'll create actual separate Linux machines — real "remote hosts" — using a free tool called **Multipass**.

### 1.1 — Install Multipass

If you already have Homebrew, run:

```
brew install --cask multipass
```

If you don't have Homebrew, just download the installer from **https://multipass.run** and run it like any Mac app. Either way, confirm it works:

```
multipass version
```

### 1.2 — Launch your first host

```
multipass launch --name host1
```

The first launch downloads an Ubuntu image, so it takes a few minutes. When it finishes, you have a running Linux virtual machine named `host1`. Find its address:

```
multipass info host1
```

Look for the **IPv4** line — something like `192.168.64.5`. Write it down; that's the IP you'll SSH to. (Yours will differ.)

### 1.3 — Put your public key on host1 (by hand, so you understand it)

Multipass gives you a shortcut door into the VM. Use it *once*, just to install your key:

```
multipass shell host1
```

Your prompt changes — you're now *inside* host1 as the user `ubuntu`. Set up the guest list:

```
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

`nano` is a simple text editor. Now you need your public key text. **Open a second Terminal tab** (`Cmd + T`) on your Mac and run:

```
pbcopy < ~/.ssh/id_ed25519.pub
```

That copies your public key to the clipboard. Switch back to the `nano` window inside host1, paste (`Cmd + V`), then press `Ctrl + O`, Enter to save, and `Ctrl + X` to exit. Lock the file's permissions and leave the VM:

```
chmod 600 ~/.ssh/authorized_keys
exit
```

> **Understand this — this trips up everyone:** SSH is picky about permissions. If `~/.ssh` or `authorized_keys` is readable by others, the server *silently refuses your key* and you'll get "Permission denied." `chmod 700` and `chmod 600` are what make it accept them. Remember this; it's the #1 cause of "it won't let me in."

### 1.4 — Connect from your Mac with your key

Back on your Mac (not inside the VM), use the IP from step 1.2:

```
ssh ubuntu@192.168.64.5 -i ~/.ssh/id_ed25519
```

You're now logged into a real, separate Linux machine using nothing but your key. Run `hostname` — it should say `host1`. Type `exit` when done.

**✅ Checkpoint 1:** You did *not* type a password. Explain what actually proved your identity to host1. (Hint: it involves the file you edited and the private key that never left your Mac.)

---

## Part 2 — Stop typing so much: the SSH config file

Typing `ubuntu@192.168.64.5 -i ~/.ssh/id_ed25519` every time is miserable. SSH has a config file that lets you define short names.

On your Mac, create/open the config:

```
nano ~/.ssh/config
```

Add this block (use *your* host1 IP):

```
Host host1
    HostName 192.168.64.5
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
```

Save and exit (`Ctrl + O`, Enter, `Ctrl + X`), then lock it down:

```
chmod 600 ~/.ssh/config
```

Now you can just run:

```
ssh host1
```

Same login, far less typing. `Host host1` is just a nickname; the lines under it fill in the details automatically.

### Your turn

Create a **second** host and add it to your config yourself — no hand-holding this time:

```
multipass launch --name host2
```

Find its IP, put your public key on it (repeat the Part 1.3 steps), then add a `Host host2` block to `~/.ssh/config`. When you can run `ssh host2` and land inside it, you've got the hang of it.

**✅ Checkpoint 2:** You now have two remote hosts you reach by name. What does the `IdentityFile` line tell SSH to do?

---

## Part 3 — The jump host (how pros reach protected servers)

In the real world, important servers usually aren't reachable directly. You first connect to a **gateway** (also called a *bastion* or *jump host*), and only from there can you reach the protected machines behind it. You'll build exactly that.

### 3.1 — Create the bastion

```
multipass launch --name bastion
```

Get its IP (`multipass info bastion`) and install your public key on it, the same way you did for host1 (Part 1.3). Add a `Host bastion` block to your `~/.ssh/config` too, and confirm `ssh bastion` works.

### 3.2 — Lock host2 down so it's only reachable through the bastion

Get into host2 the shortcut way and turn on its firewall, allowing SSH **only** from the bastion's IP (use the bastion IP from 3.1):

```
multipass shell host2
sudo ufw allow from 192.168.64.6 to any port 22
sudo ufw --force enable
exit
```

Now try to reach host2 directly from your Mac:

```
ssh host2
```

It hangs and eventually times out — host2 now refuses direct connections. That's the point.

> **Safety net:** if you ever lock yourself out with a firewall rule, `multipass shell host2` still gets you in through a side door to fix it. So you can experiment fearlessly.

### 3.3 — Jump through the bastion with ProxyJump

Edit your `~/.ssh/config` and change the `host2` block so SSH routes through the bastion. You've seen the pattern; here it is with one new line:

```
Host host2
    HostName 192.168.64.<host2-ip>
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
    ProxyJump bastion
```

Now run:

```
ssh host2
```

It works again — but this time your connection quietly travels *through* `bastion` to get there. Run `hostname` to confirm you really landed on host2.

> **Understand this:** `ProxyJump bastion` tells SSH to first open a connection to the bastion, then tunnel through it to reach host2. Your private key never touches the bastion — the login to host2 still happens from your Mac, straight through the tunnel. This is the same shape as reaching internal production servers through a single guarded entry point.

**✅ Checkpoint 3:** Explain why host2 rejected you directly but accepted you through the bastion, and what `ProxyJump` did to make that work.

---

## Definition of done

You've completed the lab when you can:

- [ ] Explain public vs. private keys without notes.
- [ ] Generate a key pair from scratch.
- [ ] Stand up a fresh Multipass host and install your key on it by hand.
- [ ] Log into it with `ssh <name>` using a config entry (no IP, no `-i`).
- [ ] Reach a firewalled host by jumping through a bastion with `ProxyJump`.

---

## Clean up when you're finished (an ops habit worth building)

Leaving VMs running wastes your laptop's memory. Stop and remove them:

```
multipass stop host1 host2 bastion
multipass delete host1 host2 bastion
multipass purge
```

`purge` permanently reclaims the space. (Only do this once you've passed the checkpoints — you'll need the hosts until then.)

---

## Stretch goals (after you've finished)

- **Add a passphrase to a key.** Generate a second key *with* a passphrase, then use `ssh-add` to load it into the macOS keychain so you're not retyping it constantly. This is what you'd actually do in the real world.
- **Set sensible defaults.** Add a `Host *` block at the top of your config with common settings that apply to every host.
- **Explore `known_hosts`.** Look at `~/.ssh/known_hosts` and figure out what got written there the first time you connected to each machine, and why SSH warns loudly if a host's fingerprint ever changes.
- **Try three hops.** Can you reach a host that's behind *two* bastions? (`ProxyJump` accepts a comma-separated chain.)

---

## Troubleshooting (read this when something breaks — it will, and that's fine)

**`Permission denied (publickey)`** — the most common one. Check, in order: is your public key actually in that host's `~/.ssh/authorized_keys`? Are the permissions right (`chmod 700 ~/.ssh`, `chmod 600 ~/.ssh/authorized_keys`)? Are you using the right username (`ubuntu`) and the matching `IdentityFile`?

**`Connection refused`** — usually the SSH server isn't running or you've got the wrong IP. Re-check the IP with `multipass info <name>` (VM IPs can change after a restart — if a host stops working after a reboot, update its IP in `~/.ssh/config`).

**It just hangs / times out** — a firewall (like the one you set in Part 3) is blocking you, or the host is off. Expected for host2 in Part 3; use `multipass shell` as your side door.

**`REMOTE HOST IDENTIFICATION HAS CHANGED`** — you rebuilt a host that's reusing an old IP, so its fingerprint doesn't match what's stored. The error message tells you the exact command to remove the stale entry from `known_hosts`; run it, then reconnect.

**Lost inside a VM and want out** — type `exit`. If a session is truly stuck, press `~` then `.` (tilde, then period) to force-close an SSH session.

---

## Show your mentor (final checkpoint)

Demonstrate three things live: `ssh host1` landing you on host1, `ssh host2` reaching host2 *through the bastion*, and — with your config file open — walk through what each line does. Then explain, in your own words, the public/private key idea and what `authorized_keys` is for. If you can do that, you haven't just followed steps; you've learned SSH.
