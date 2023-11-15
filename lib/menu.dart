import 'package:flutter/material.dart';
import 'package:light_cones_mobile/form.dart';
import 'package:light_cones_mobile/left_drawer.dart';

class MainMenu extends StatelessWidget {
  const MainMenu({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tugas 7 PBP')),
      drawer: const LeftDrawer(),
      body: Container(
        margin: const EdgeInsets.all(32.0),
        child: GridView.count(
          crossAxisCount: 2,
          mainAxisSpacing: 32.0,
          crossAxisSpacing: 32.0,
          children: const [
            MenuButton(text: "Lihat Item", iconData: Icons.remove_red_eye),
            MenuButton(text: "Tambah Item", iconData: Icons.add),
            MenuButton(text: "Logout", iconData: Icons.logout),
          ],
        ),
      ),
    );
  }
}

class MenuButton extends StatelessWidget {
  final IconData iconData;
  final String text;

  const MenuButton({super.key, required this.text, required this.iconData});

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.blue,
      child: InkWell(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              iconData,
              color: Colors.white,
              size: 30.0,
            ),
            Text(
              text,
              textAlign: TextAlign.center,
              style: const TextStyle(color: Colors.white),
            ),
          ],
        ),
        onTap: () {
          if (text == "Tambah Item") {
            Navigator.push(
              context, MaterialPageRoute(
                builder: (context) => const FormPage(),
              )
            );
          }
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              duration: const Duration(seconds: 2),
              content: Text(
                "Kamu telah menekan tombol $text!",
                textAlign: TextAlign.left,
                style: const TextStyle(color: Colors.white),
              ),
            ),
          );
        },
      ),
    );
  }
}
